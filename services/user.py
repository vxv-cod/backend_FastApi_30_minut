from models.user import User
from sqlalchemy.orm import Session
from dto import user
# from dto.user import User 

# def respo(data):
#     response = make_response(json.dumps(data, ensure_ascii = False, indent=4, sort_keys=True))
#     response.headers['Content-Type'] = 'application/json; charset=utf-8'
#     return response
        
        

def create_user(data: user.User, db):
    user = User(name = data.name)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    
    return user


def get_user_all(db):
    return db.query(User).all()


def get_user(id: int, db):
    return db.query(User).filter(User.id == id).first()


def update(data: user.User, db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    user.name = data.name
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def remove(db: Session, id: int):
    user = db.query(User).filter(User.id == id).delete()
    db.commit()
    return user
    
