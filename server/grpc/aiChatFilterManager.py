import postgres
import threading

class aiChatFilterManager: 
    def __init__(self, postgres: postgres.postgres):
        self.maxCount = postgres.getAIMaxLoopCount()
        self.words = postgres.getAIChatFilter()
        self.ages = postgres.getAgentAgeGroups()
        self.postgres = postgres
        self.thread = threading.Timer(35.0, self.update)
        self.thread.start()
  
    
    def update(self):
        print('getting new')
        self.maxCount = self.postgres.getAIMaxLoopCount()
        self.words = self.postgres.getAIChatFilter()
        self.ages = self.postgres.getAgentAgeGroups()

    def hasBadWord(self, text, agent):
        agegroup = self.getAgentAge(agent)
        for x in self.words:
            if (agegroup == x['age'] and  (x['word'] in text or x['word'] == 'unlimited')):
                return True
        
        return False
    
    def getAgentAge(self, agent):
        for a in self.ages:
            if agent == a['agent']:
                return a['age'][0] if len(a['age']) > 0 else '19'

    def getMaxCount(self):
        return self.maxCount