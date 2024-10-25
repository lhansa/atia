# ATiA

**A**pp **Ti**me **A**nalytics is not even an app, it is just Python code that reads the logs of the apps you use and gives you a report of how much time you spend on each app.

For now, it is just that. But perhaps someday it'll include some analytics based on this data. 

## How to use

1. Clone this repository
2. Run the script `python3 cli.py start d` to start the logger, where `d` is the time interval in seconds. For example, `python3 cli.py start 120` will log the apps you use during 2 minutes.
3. Use your computer as you normally would
4. Run the script `python3 cli.py report` after the time period to get a _report_ on the apps you used during that time.

Bear in mind that the report is no sophisticated at all. It is just a list of the apps you used and the time you spent on each one.

### Example of results

```
Informe de uso de aplicaciones:
app
Code              0:07:37
Google-chrome     0:00:17
Xfce4-terminal    0:00:00
```

## Details

The app tracks 2 things:

1. The app you're using. 
2. If it is Google Chrome, the domain you're navigating to.

