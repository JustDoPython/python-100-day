import os
import logging

class Config:
    ## 管理员邮件
    MAIL_USERNAME = 'username'
    MAIL_PASSWORD = 'Pa$sw0rd'
    MAIL_USE_TLS = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = '465'
    FLASKY_MAIL_SENDER = 'flaskyserver@163.com'
    FLASKY_ADMIN = 'flaskyadmin@163.com'
    FLASKY_MAIL_SUBJECT_PREFIX = '服务器又挂啦'
    LOG_FILENAME = 'flasky.log'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        super().init_app(app)


class TestingConfig(Config):
    TESTING = True
    @classmethod
    def init_app(cls, app):
        super().init_app(app)
        
        formatter = logging.Formatter('%(asctime)s - %(threadName)s - %(levelname)s - [line:%(lineno)d] - %(funcName)s - %(message)s')
        file_handler = logging.FileHandler(cls.LOG_FILENAME, mode='a', encoding='utf-8', delay=False)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        app.logger.addHandler(file_handler)


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        super().init_app(app)

        from logging.handlers import SMTPHandler

        credentials = None
        secure = None

        if getattr(cls, 'MAIL_USERNAME', None):
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' APPLICATION ERROR',
            credentials=credentials,
            secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
