from webnodes import WebNode

from simpletodo.models import Todo


class CPT_List(WebNode):
    template = 'components/list.html'

    def get_context(self, a, b, x=None, y=None):
        todos = Todo.objects.all().order_by('finished', '-id')
        return {'todos': todos}


class CPT_ITEM(WebNode):
    template = 'components/item.html'

    def get_context(self, todo):
        return {'todo': todo}


class CPT_Add(WebNode):
    template = 'components/add.html'
