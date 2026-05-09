from mrjob.job import MRJob
class MRFraudTransactionCount(MRJob):
        def mapper(self, _, line):
                
                 
                data = line.split(',')
                transaction_id = data[0] 
                is_fraud =data[2]#assuming 1 for fraud ,0 for legitimate
                #Yield fraudulent transactions
                if is_fraud == '1':
                        yield('fraud',line)
        def reducer(self,key,values):
                #sum up all fraudulent transactions
                
                   yield(key,sum(values))
if __name__ =='__main__':
     MRFraudTransactionCount.run()
            