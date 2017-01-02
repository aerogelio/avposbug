import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import ActionButton

from kivy.lang import Builder
Builder.load_string('''
<ActionExample>
    name: 'Main'
    orientation: 'vertical'
    ActionBar:
        ActionView:
            id: avButtons
            ActionPrevious:
    BoxLayout:
        size_hint: 1, None
        size: 1, 40
    BoxLayout:
        size_hint: 1, None
        size: 1, 40
        Button:
            text: 'Clear'
            on_release: root.clear()
        Button:
            text: 'Add'
            on_release: root.add()
        Button:
            text: 'Remove'
            on_release: root.remove()
    BoxLayout:
''')

class ActionExample(BoxLayout):
    
    def add(self):
        num = len(self.ids.avButtons.children)
        abAction = ActionButton( text='Do some...' + str(num) )
        self.ids.avButtons.add_widget( abAction )
    
    def remove(self):
        #prevent elimination ActionPrevious
        if len(self.ids.avButtons.children) > 1:
            widget = self.ids.avButtons.children[0]
            self.ids.avButtons.remove_widget( widget )
        
    def clear(self):
        #prevent elimination ActionPrevious
        if len(self.ids.avButtons.children) > 1:
            children = self.ids.avButtons.children[:-1]
            self.ids.avButtons.clear_widgets( children=children)

class MainApp(App):
    
    def build(self):
        
        return ActionExample()


if __name__ == '__main__':
    MainApp().run()