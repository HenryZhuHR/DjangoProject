import os


# https://www.cnblogs.com/freely/p/10223681.html
def get_logging_setting(base_dir: str):
    BASE_LOG_DIR = os.path.join(base_dir, "logs")
    os.makedirs(BASE_LOG_DIR, exist_ok=True)

    run_log = os.path.join(BASE_LOG_DIR, 'run.log')
    info_log=os.path.join(BASE_LOG_DIR, "info.log")
    error_log = os.path.join(BASE_LOG_DIR, 'error.log')

    return {
        'version': 1,  # 保留字
        'disable_existing_loggers': False,  # 禁用已经存在的logger实例

        # 日志文件的格式
        'formatters': {
            # 详细的日志格式
            'standard': {
                'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                '[%(levelname)s][%(message)s]'
            },
            # 简单的日志格式
            'simple': {
                'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
            },
            # 定义一个特殊的日志格式
            'collect': {
                'format': '%(message)s'
            }
        },

        # 过滤器
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },

        # 处理器
        'handlers': {
            # 在终端打印
            'console': {
                'level': 'DEBUG',
                # 只有在Django debug为True时才在屏幕打印日志
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',  #
                'formatter': 'simple'
            },

            # 默认的
            'default': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
                'filename': os.path.join(BASE_LOG_DIR, "info.log"),  # 日志文件
                'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
                'backupCount': 3,  # 最多备份几个
                'formatter': 'standard',
                'encoding': 'utf-8',
            },

            # 输出到文件
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': run_log,
            },

            # 专门用来记错误日志
            'error': {
                'level': 'ERROR',
                'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
                'filename': os.path.join(BASE_LOG_DIR, "error.log"),  # 日志文件
                'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
                'backupCount': 5,
                'formatter': 'standard',
                'encoding': 'utf-8',
            },

            # 专门定义一个收集特定信息的日志
            'collect': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
                'filename': os.path.join(BASE_LOG_DIR, "collect.log"),
                'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
                'backupCount': 5,
                'formatter': 'collect',
                'encoding': "utf-8"
            }

        },
        
        'loggers': {
            # 默认的logger应用如下配置
            '': {
                # 上线之后可以把'console'移除
                'handlers': [
                    'default', 
                    'console', 
                    'error'
                    ],
                'level': 'DEBUG',
                'propagate': True,  # 向不向更高级别的logger传递
            },
            
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            # 名为 'collect'的logger还单独处理
            'collect': {
                'handlers': ['console', 'collect'],
                'level': 'INFO',
            }
        },
    }
