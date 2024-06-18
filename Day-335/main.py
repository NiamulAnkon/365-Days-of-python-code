import pandas as pd
from collections import Counter
import re

class feedback_analyzie:
    def customer_feedback_summary(self):
        customer_feedback = {
            'Customer ID': [1, 2, 3, 4, 5],
            'Feedback Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
            'Rating': [5, 3, 1, 4, 2],
            'Feedback Text': [
                'Excellent service, very happy!',
                'Okay, but room for improvement.',
                'Very dissatisfied, poor quality.',
                'Good, but delivery was late.',
                'Not satisfied with the product.'
            ]
        }
        data = pd.DataFrame(customer_feedback)
        avrg_rating = data['Rating'].mean()
        all_fdbck_entries = data.shape[0]
        highest_rating_feedback = data.loc[data['Rating'].idxmax()]['Feedback Text']
        lowest_rating_feedback = data.loc[data['Rating'].idxmin()]['Feedback Text']
        positive_feedback_percentage = (data[data['Rating'] >= 4].shape[0] / all_fdbck_entries) * 100
        neutral_feedback_percentage = (data[data['Rating'] == 3].shape[0] / all_fdbck_entries) * 100
        negative_feedback_percentage = (data[data['Rating'] <= 2].shape[0] / all_fdbck_entries) * 100
        feedback_text = ' '.join(data['Feedback Text']).lower()
        words = re.findall(r'\b\w+\b', feedback_text)
        common_words = Counter(words).most_common()
        print(f"The Avrage Rating is: {avrg_rating}\nnumber of feedback entries: {all_fdbck_entries}\nFeedback with highest rating is: {highest_rating_feedback}\nFeedback with positive rating is: {positive_feedback_percentage}\nFeedback with neutral rating is: {neutral_feedback_percentage}\nFeedback with Lowest rating is: {lowest_rating_feedback}\nFeedback with negative rating is: {negative_feedback_percentage}\nCommon Words in Feedback: {common_words}")


if __name__ == "__main__":
    fa = feedback_analyzie()
    fa.customer_feedback_summary()