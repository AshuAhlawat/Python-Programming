headlines=["Local Bear Eaten by Man","Legistature Announces New Laws","Peasant Discovers Violence Inherent in System","Car Rescues Fireman Stuck in Tree","Brave Knight Runs Away","Papperbok Review: Totally Triffic"]
news_ticker=" "
for line in headlines:
    news_ticker+=line +" "
    if len(line)>=140:
        news_ticker=news_ticker[:140]
        break
print(news_ticker)