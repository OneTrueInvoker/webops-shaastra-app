import re
import random_responses


# Load JSON data


# Store JSON data
response_data = [
  {
    "response_type": "greeting",
    "user_input": ["hello", "hi", "hey"],
    "bot_response": "Hey there!",
    "required_words": []
  },
  {
    "response_type": "greeting",
    "user_input": ["see you", "goodbye", "bye"],
    "bot_response": "See you later!",
    "required_words": []
  },
  {
    "response_type": "greeting",
    "user_input": ["nice", "to", "meet", "you"],
    "bot_response": "The pleasure is all mine!",
    "required_words": ["nice", "meet", "you"]
  },
  {
    "response_type": "question",
    "user_input": ["may","I","know","my","grade","grades","for","maths","physics","Chemistry","language",],
    "bot_response": "Sure, please enter your marks",
    "required_words": []
  },
  {
    "response_type": "question",
    "user_input": ["my","marks","for","91","91","92","93","94","95","96","97","98","99","100"],
    "bot_response": "Your grade is S\ndo you wish to continue",
    "required_words": []
  },

  {
    "response_type": "question",
    "user_input": ["my","marks","for","81","81","82","83","84","85","86","87","88","89","90"],
    "bot_response": "Your grade is A\ndo you wish to continue",
    "required_words": []
  },
  {
    "response_type": "question",
    "user_input": ["my","marks","for","71","71","72","73","74","75","76","77","78","79","80"],
    "bot_response": "Your grade is B\ndo you wish to continue",
    "required_words": []
  },
  {
    "response_type": "question",
    "user_input": ["my","marks","for","61","61","62","63","64","65","66","67","68","69","70"],
    "bot_response": "Your grade is C\n do you wish to continue",
    "required_words": []
  },
  {
    "response_type": "question",
    "user_input": ["my","marks","for","51","51","52","53","54","55","56","57","58","59","60"],
    "bot_response": "Your grade is D\ndo you wish to continue",
    "required_words": []
  },
  {
    "response_type": "question",
    "user_input": ["my","marks","for","41","41","42","43","44","45","46","47","48","49","50"],
    "bot_response": "Your grade is E\ndo you wish to continue",
    "required_words": []
  },

  {
    "response_type": "question",
    "user_input": ["marks","my","for"'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40'],
    "bot_response": "Sorry, you have failed\ndo you wish to continue",
    "required_words": []
  },

  {
    "response_type": "question",
    "user_input": ["how", "are", "you"],
    "bot_response": "I'm great! Thanks for asking.",
    "required_words": ["how", "are", "you"]
  },

  {
      "response_type": "question",
      "user_input":["yes"],
      "bot_response":"Please ask your next question",
      "required_words":[]
  },
  {
      "response_type": "question",
      "user_input":["no"],
      "bot_response":"Thank you for using the ChatBot, see you next time :)",
      "required_words":[]
  }
]


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]
    
    return random_responses.random_string()



while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))
