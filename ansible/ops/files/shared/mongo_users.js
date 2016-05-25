var helper = {};
helper.use = function( dbname ){
    db = db.getMongo().getDB( dbname );
    print( "switched to db " + db.getName() );
};

db.auth('muxi', '#dev@muxi5');
var user_exist = db.getUser("muxi");

if (user_exist){
    db.auth('muxi', '#dev@muxi5');
} else{
    db.createUser({ user: 'muxi', pwd: '#dev@muxi5', roles: [ { role: "root", db: "admin" } ] });
}

var projects = ['merchant', 'transaction'];

// Creating merchant user;
projects.forEach(function(project) {
    helper.use(project);
    if(db.getUser(project)){
        print('User ' + project + ' already exists');
    }else{
        db.createUser({ user: project, pwd: 'MUXI2016'+project, roles: [ { role: "readWrite", db: project } ] });
        print( project + ' user created.');
    }
});
db.createUser({ user: 'merchant', pwd: 'MUXI2016merchant', roles: [ { role: "readWrite", db: 'merchant' } ] });
