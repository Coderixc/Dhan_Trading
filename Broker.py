from dhanhq import dhanhq

class Client_DhanHQ:
    BrokerName = "DHANHQ"
    AcessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzA0NTI5OTA5LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMTkyNTA0MiJ9.QGgnQ2aSu1XmAorfzIF1ik0Z4J9vBxKTSM_rCq3sEivgYIvN9RUYycAdFZxmLGrdRvJoivkAZs9vDoS9KciVeA"
    ClientCode = "1101925042"



class DhanTradingApi:
    print("Initializing Broker API...")

    def __init__( self ):
        self.Bname= Client_DhanHQ.BrokerName
        self.AcessToken = Client_DhanHQ.AcessToken
        self.ClintCode = Client_DhanHQ.ClientCode


        """ Next Func """
        self.Prepare_Connection()

    def Prepare_Connection( self ):
        try:
            dhan = dhanhq(self.ClintCode,self.AcessToken)
            print(dhan)

            dd =dhan.get_holdings( )
            print(dd)

            p=dhan.place_order( security_id = '1333' ,  # hdfcbank
                              exchange_segment = dhan.NSE ,
                              transaction_type = dhan.BUY ,
                              quantity = 10 ,
                              order_type = dhan.MARKET ,
                              product_type = dhan.INTRA ,
                              price = 0
                              )

            print(p)

            z = dhan.get_fund_limits()
            print(z)

            """  get Quote"""
            

        except Exception as e:
            print(f"Error(s) Generated While Connection to Broker {self.Bname} , Error {e}")


