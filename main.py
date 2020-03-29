from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from api import authenticate,addUser

class LoginPage(Screen):
    def verify_credentials(self):
        user = self.ids['login'].text
        password = self.ids['passw'].text
        if not authenticate(user,password).json()==200:
            self.ids['login'].text = ""
            self.ids['passw'].text = ""
            self.manager.current = "CameraClick"
        else:
            self.ids['login'].text = ""
            self.ids['passw'].text = ""
            self.manager.current = "user"

class SignUpPage(Screen):
    def authenticate_credentials(self):
        user = self.ids['login'].text
        password=self.ids['passw'].text
        name = self.ids['name'].text
        addUser(user,password,name)

class UserPage(Screen):
    pass

class CameraClick(Screen):
    def build(self):

        layout = BoxLayout(orientation='vertical')

       

        # Create a camera object

        self.cameraObject            = Camera(play=False)

        self.cameraObject.play       = True

        self.cameraObject.resolution = (300, 300) # Specify the resolution

       

        # Create a button for taking photograph

        self.camaraClick = Button(text="Take Photo")

        self.camaraClick.size_hint=(.5, .2)

        self.camaraClick.pos_hint={'x': .25, 'y':.75}

 

        # bind the button's on_press to onCameraClick

        self.camaraClick.bind(on_press=self.onCameraClick)

       

        # add camera and button to the layout

        layout.add_widget(self.cameraObject)

        layout.add_widget(self.camaraClick)

       

        # return the root widget

        return layout

 

    # Take the current frame of the video as the photo graph       

    def onCameraClick(self, *args):

        self.cameraObject.export_to_png('/kivyexamples/selfie.png')


class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file('login.kv')

class LoginApp(App):
    def builder(self):
        return kv_file

if __name__ == '__main__':
    LoginApp().run()