class Config:
    @staticmethod
    def init_app():
        pass

class Development_config(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://mali9810:M123456@localhost/compos1'
    UPLOAD_FOLDER = 'static/images'

class Production_config(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://mali9810:M123456@localhost/compos1'
    UPLOAD_FOLDER = 'static/images'

projectConfig={
    'dev': Development_config,
    'pro':Production_config
}