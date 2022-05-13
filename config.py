class Config:
    SECRET_KEY='admin'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='admin'
    MYSQL_DB='flask_login'

config={
    'development':DevelopmentConfig
}