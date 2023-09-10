import datetime
from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import schemas

from .. import models, database, schemas, utils, oauth2
router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.post('/new-blog',status_code=status.HTTP_201_CREATED, response_model=schemas.BlogOut) 
def create_new_blog(blog: schemas.BlogCreate, db: Session = Depends(database.get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    blog = models.Blog(user_id = current_user.id,**blog.model_dump())
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

@router.get('/get-all-blogs',status_code=status.HTTP_200_OK)
def get_all_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f' blogs not found')
    return blogs

@router.get('/get-blog/{id}',status_code=status.HTTP_200_OK)
def get_blog(id:int,db: Session = Depends(database.get_db),current_user: int = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.blog_id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id}, blog not found')
    return blog

@router.get('/get-blogs-current-user',status_code=status.HTTP_200_OK)
def get_blog_ownerid(db: Session = Depends(database.get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).filter(models.Blog.user_id == current_user.id).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{current_user.id},no blog not found')
    return blogs

@router.get('/get-blogs-users/{id}',status_code=status.HTTP_200_OK)
def get_blog_ownerid(id:int,db: Session = Depends(database.get_db),
                     current_user: int = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).filter(models.Blog.user_id == id).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id},users blog not found')
    return blogs

@router.put('/update-post/{id}',status_code=status.HTTP_200_OK)
def update_post(id:int,blog: schemas.BlogCreate, db: Session = Depends(database.get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    update_query = db.query(models.Blog).filter(models.Blog.blog_id == id)
    update_blog = update_query.first()
    if not update_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id},users blog not found')
    if update_blog.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='not authorized')
    update_query.update(blog.model_dump(), synchronize_session=False)
    db.commit()
    return update_query.first()

@router.delete('/delete-blog/{id}')
def delete_blog(id:int, db: Session = Depends(database.get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    deleted_blog = db.query(models.Blog).filter(models.Blog.blog_id == id)
    blog_delete = deleted_blog.first()
    if blog_delete == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'{id}, record not found')
    if blog_delete.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail='not authorized')
    deleted_blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)