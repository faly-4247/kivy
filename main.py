from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp


class MonApplication(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=dp(30),
            spacing=dp(15)
        )

        self.titre = Label(
            text="Bienvenue dans mon application",
            font_size="22sp",
            size_hint_y=None,
            height=dp(70)
        )

        self.champ_nom = TextInput(
            hint_text="Entrez votre nom",
            multiline=False,
            size_hint_y=None,
            height=dp(50)
        )

        bouton = Button(
            text="Valider",
            size_hint_y=None,
            height=dp(50)
        )

        self.message = Label(
            text="Veuillez saisir votre nom.",
            font_size="18sp"
        )

        bouton.bind(on_press=self.valider_nom)

        layout.add_widget(self.titre)
        layout.add_widget(self.champ_nom)
        layout.add_widget(bouton)
        layout.add_widget(self.message)

        return layout

    def valider_nom(self, instance):
        nom = self.champ_nom.text.strip()

        if nom:
            self.message.text = f"Bonjour {nom} ! Bienvenue."
        else:
            self.message.text = "Veuillez saisir votre nom."


if __name__ == "__main__":
    MonApplication().run()