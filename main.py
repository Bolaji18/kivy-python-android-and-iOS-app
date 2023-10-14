from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        # you create a list of
        # operators and a couple of handy values, last_was_operator and last_button, that you’ll use later on.
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        #you create a top-level layout main_layout and add a read-only TextInput widget to it.
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        #you create a nested list of lists containing most of your buttons for the calculator.
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        #you start a for loop over those buttons. For each nested list you’ll do the following:
        for row in buttons:
            # you create a BoxLayout with a horizontal orientation
            h_layout = BoxLayout()
            #you start another for loop over the items in the nested list.
            for label in row:
                #you create the buttons for the row, bind them
                # to an event handler, and add the buttons to the horizontal BoxLayout from line 23
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
                #you add this layout to main_layout.
            main_layout.add_widget(h_layout)
          # you create the equals button (=), bind it to an event handler, and add it to main_layout.
        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout
 #takes the instance argument so you can access which widget called the function.
    def on_button_press(self, instance):
        #extract and store the value of the solution and the button text.
        current = self.solution.text
        button_text = instance.text
       #check to see which button was pressed. If the user pressed C,
        # then you’ll clear the solution. Otherwise, move on to the else statement.
        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            #checks if the solution has any pre-existing value.
            #check if the last button pressed was an operator button. If it was, then solution won’t be updated.
            # This is to prevent the user from having two operators in a row. For example, 1 */ is not a valid statement.
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            #check to see if the first character is an operator. If it is,
            # then solution won’t be updated, since the first value can’t be an operator value.
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            #drop to the else clause. If none of the previous conditions are met, then update solution.
            else:
                new_text = current + button_text
                self.solution.text = new_text
                #sets last_button to the label of the last button pressed.
        self.last_button = button_text
        #sets last_was_operator to True or False depending on whether or not it was an operator character.
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()