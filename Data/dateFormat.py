def monthToNum(shortMonth):  
        return{
                'January' : "01",
                'February' : "02",
                'March' : "03",
                'April' : "04",
                'May' : "05",
                'June' : "06",
                'July' : "07",
                'August' : "08",
                'September' : "09", 
                'October' : "10",
                'November' : "11",
                'December' : "12",
                'Jan' : "01",
                'Feb' : "02",
                'Mar' : "03",
                'Apr' : "04",
                'May' : "05",
                'Jun' : "06",
                'Jul' : "07",
                'Aug' : "08",
                'Sep' : "09", 
                'Oct' : "10",
                'Nov' : "11",
                'Dec' : "12",
        }[shortMonth]

def dayFormat(day):
        if len(day) == 1:
	       return("0"+day)
        return(day)

def formatDayName(dayname):
        return dayname[0:3]