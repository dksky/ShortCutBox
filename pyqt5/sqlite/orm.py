from peewee import *

db = SqliteDatabase('ShortcutBox.db')

class BaseModel(Model):
  createBy = CharField(null=True)
  createDate = DateTimeField(null=True)
  modifyBy = CharField(null=True)
  modifyDate = DateTimeField(null=True)
  isDeleted = BooleanField()
  class Meta:
    database = db

class Menu(BaseModel):
  id = PrimaryKeyField()
  name = CharField(null = False)
  description = CharField()
  #parentId = ForeignKeyField(Menu,to_field='id',related_name = "menu")
  parentId = IntegerField(null = True)
  isLeaf = BooleanField()
  isSystemMenu = BooleanField()
  order = IntegerField()
  class Meta:
    order_by = ('id',)
    db_table = 'menu'

class Folder(BaseModel):
  id = PrimaryKeyField()
  name = CharField(null=False)
  class Meta:
    order_by = ('id',)
    db_table = 'folder'

class Plugin(BaseModel):
  id = PrimaryKeyField()
  name = CharField(null=False)
  description = CharField()
  type = CharField()
  class Meta:
    order_by = ('id',)
    db_table = 'plugin'

class PluginFunc(BaseModel):
  id = PrimaryKeyField()
  pluginId = ForeignKeyField(Plugin, to_field='id', related_name="plugin")
  name = CharField(null=False)
  description = CharField()
  type = CharField()
  commandPrefix = CharField()
  commandFile = CharField()
  commandParams = CharField()
  class Meta:
    order_by = ('id',)
    db_table = 'pluginFunc'

class PluginFuncFormEle(BaseModel):
  id = PrimaryKeyField()
  pluginFuncId = ForeignKeyField(PluginFunc, to_field='id', related_name="pluginFunc")
  labelName = CharField(null=False)
  varName = CharField(null=False)
  description = CharField()
  type = CharField()
  json = CharField()
  class Meta:
    order_by = ('id',)
    db_table = 'pluginFuncFormEle'

class Application(BaseModel):
  id = PrimaryKeyField()
  name = CharField(null = False)
  folderId = ForeignKeyField(Folder,to_field='id',related_name = "folder", null = True)
  pluginId = ForeignKeyField(Plugin,to_field='id',related_name = "plugin")
  pluginFuncId = ForeignKeyField(PluginFunc, to_field='id', related_name="pluginFunc")
  class Meta:
    order_by = ('id',)
    db_table = 'application'

class ApplicationConfig(BaseModel):
  id = PrimaryKeyField()
  applicationId = ForeignKeyField(Application,to_field='id',related_name = "application")
  name = CharField(null=False)
  value = CharField(null=True)
  class Meta:
    order_by = ('id',)
    db_table = 'applicationConfig'

