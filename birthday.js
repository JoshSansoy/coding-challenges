function run (birthday_date){

    endDate = 2066;
	
	birthday_date = birthday_date.split('-').reverse().join('-');
	
    const DAYS = {
        0: 'Sun',
        5: 'Fri',
        6: 'Sat',
    }
	
	let leapDay = false;
	if (birthday_date === '02-29'){
		leapDay = true;
	}
	
    future_dates_array = [];

	
    for(let year = 2016; year < endDate; year++){
    	
    	const isLeap = year % 100 === 0 ? year % 400 === 0 : year % 4 === 0;
    	
        birthday = year + "-" + birthday_date;
        const d = new Date(birthday);
        day = d.getDay();
        if ((day === 0 || day >= 5) && !leapDay){
            future_dates_array.push(DAYS[day] + '-' + year);
        }
        
        if ((day === 0 || day >= 5) && leapDay && isLeap){
        	future_dates_array.push(DAYS[day] + '-' + year);
        }
    }
   
    future_dates = future_dates_array.join(' ');
	return future_dates;
}

console.log(run("29"))