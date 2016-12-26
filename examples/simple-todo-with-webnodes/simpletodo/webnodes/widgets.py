from webnodes import WebNode

from simpletodo.models import Todo


class ListNode(WebNode):
    template = 'components/list.html'

    def get_context(self):
        todos = Todo.objects.all().order_by('finished', '-id')
        return {'todos': todos}


class ItemNode(WebNode):
    template = 'components/item.html'

    def get_context(self, todo):
        return {'todo': todo}


class AddNode(WebNode):
    template = 'components/add.html'
