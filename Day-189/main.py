import speech_recognition as sr
import requests
import pyttsx3
import re
import requests

class CurrencyConverter:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.api_key = "6a70a7c204ce71cd39a45846"
        self.currency_url = f"https://open.er-api.com/v6/latest/{self.api_key}"

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def get_audio(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Please say something...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("Recognizing...")

        try:
            recognized_text = recognizer.recognize_google(audio, language="en-US")
            print("You said:", recognized_text)

            numeric_part = re.search(r'\b\d+\b', recognized_text)
            if numeric_part:
                return numeric_part.group()
            else:
                print("No numeric value found.")
                return None

        except sr.UnknownValueError:
            print("Sorry, I could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None


    def convert_currency(self, amount, from_currency, to_currency):
        if from_currency is None or to_currency is None:
            print("Invalid currency codes.")
            return

        try:
            amount = float(amount)
            conversion_url = f"{self.currency_url}?q=1&from={from_currency.upper()}&to={to_currency.upper()}"
            response = requests.get(conversion_url)
            data = response.json()
            rate = data["results"]["1{from}_{to}".format(from_currency.upper(), to_currency.upper())]["val"]
            converted_amount = amount * rate

            print(f"{amount} {from_currency.upper()} is equal to {converted_amount:.2f} {to_currency.upper()}")
        except ValueError:
            print("Invalid amount. Please provide a numeric value.")
        except KeyError:
            print("Invalid currency codes. Please check the provided currency codes.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def run(self):
        self.speak("Welcome to the Currency Converter. How can I assist you today?")

        while True:
            self.speak("Please state the amount you want to convert.")
            amount = float(self.get_audio())

            self.speak("Please state the source currency.")
            from_currency = self.get_audio()

            self.speak("Please state the target currency.")
            to_currency = self.get_audio()

            self.convert_currency(amount, from_currency, to_currency)

            self.speak("Do you want to perform another conversion? Yes or No")
            response = self.get_audio()

            if response and "no" in response:
                self.speak("Thank you for using the Currency Converter. Have a great day!")
                break
            elif not response or "yes" not in response:
                self.speak("Invalid response. Exiting.")
                break

if __name__ == "__main__":
    converte_curency = CurrencyConverter()
    converte_curency.run()
