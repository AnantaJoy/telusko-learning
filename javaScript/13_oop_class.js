var stdInfo = {
     name: "Ananta Asim Joy",
     stdId: "1810174145",
     Dept: "EEE",
     Session: '2017-18',

 }

console.log(stdInfo);

function stdInfoUpdated(std_name,std_id,std_dept,std_session){
    this.std_name = std_name;
    this.std_id = std_id;
    this.std_dept = std_dept;
    this.std_session = std_session;

    //return console.log(std_name,std_id,std_dept,std_session);
}

var std_1 = new stdInfoUpdated('Ananta Asim Joy', 1810174145,'EEE','2017-18');
var std_2 = new stdInfoUpdated('Imtiaz Ahamed Fuad', 1810174135,'CSE','2018-19');

console.log(std_1.std_name);
console.log(std_2.std_name);
// console.log(typeof(stdInfoUpdated));

stdInfo.Hall = "Sher-e-Bangla";
console.log(stdInfo);
console.log(typeof(stdInfo));