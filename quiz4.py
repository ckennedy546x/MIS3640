ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}





class Candidate:

    """The presidential candidate"""



    def __init__(self, passing_name = 'Unknown', winning_states_pass=None, votes_pass=0):

        """Initialize candidate.



        name: string

        winning_states: a list of strings representing initial winning state(s).

        votes: integer, representing number of votes

        """

        self.name = passing_name
        self.winning_states = winning_states_pass
        self.votes = votes_pass




    def __str__(self):

        """Return a string representaion of this candidate,

        including name and winning state(s).

        """

        return '{} won the states of {} with {} votes.'.format(self.name, self.winning_states, self.votes)



    def win_state(self, state):

        """Adds a state to winning_states and updates votes.



        state: a string of state abbreviation

        """
        trump.winning_state = []
        clinton.winning_state = []
        if self.name == trump:
            trump.winning_state.append(state)
        elif self.name == clinton:
            clinton.winning_state.append(state)

    def __gt__(self, another_self):
        return trump.votes > clinton.votes


def main():

    trump = Candidate('Donald Trump')

    clinton = Candidate('Hillary Clinton', winning_states=['CA'], votes=55)

    print(trump)

    print(clinton)

    print()

    print('After election:')

    trump.win_state('FL')

    trump.win_state('TX')

    clinton.win_state('MA')

    print(trump)

    print(clinton)

    print('Does Trump win?')

    print(trump > clinton)



if __name__ == '__main__':

    main()