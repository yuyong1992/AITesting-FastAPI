# AITesting-FastAPI
接口测试平台，基于python FastAPI 框架

#### 开发过程
1. settings 读取config文件组装SqlAlchemy的MySQL连接URI
2. db 创建SqlAlchemy的数据库连接引擎以及数据库SessionMaker
3. 创建与数据库表映射的models
4. 创建CRUD的基类，继承基类并分别实现不同model的CRUD
5. 根据业务实现路由接口
6. 创建各个接口入参和返回结果的模式 schema
7. 将路由注册到App
