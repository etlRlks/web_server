from models.model_basic import Model, SQLModel
from models.comment import Comment
from models.user import User
from utils import log


class Weibo(SQLModel):
    """
    微博类:
        重构，注释了add和update方法
    """

    def __init__(self, form):
        super().__init__(form)
        # self.id = form.get('id', None)
        self.content = form.get('content', '')
        # 和别的数据关联的方式, 用 user_id 表明拥有它的 user 实例
        self.user_id = form.get('user_id', None)

    def comments(self):
        # log('self id', self.id)
        cs = Comment.all(weibo_id=self.id)
        return cs

    def user(self):
        u = User.one(id=self.user_id)
        return u

    # @classmethod
    # def add(cls, form, user_id):
    #     w = Weibo(form)
    #     w.user_id = user_id
    #     w.save()

    # @classmethod
    # def update(cls, id, content):
    #     w = Weibo.find_by(id=id)
    #     w.content = content
    #     w.save()
