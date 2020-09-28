function insertUser(name, usr, pwd, grp, org) {
    try {
        query = {
            "name":name, 
            "username":usr, 
            "password":pwd, 
            "group":grp, 
            "organization":org
        }

        // Check for duplicate, create new if unique
        db.accounts.update(query, query, true)
        print("Successful Account Insert")
    } catch(err){
        print(err)
    }
}

function deleteUser(name) {
    try {
        query = {
            "name":name
        }

        // Check for duplicate, create new if unique
        db.accounts.deleteOne(query)
        print("Successful Account Deletion")
    }catch(err) {
        print(err)   
    }
}

function viewAccounts() {
    db.accounts.find()
}

// Usage
// insertUser("Natty B", "test", "tst", "ADMIN", "WEBER")
// deleteUser("Natty B")

// Initial Data
insertUser("Steve Everworth", "sever99", "password", "USER", "Virginia Tech")
insertUser("Alexander Wendover", "a1wen", "securePA33", "INSTRUCTOR", "Virginia Tech")
insertUser("Alan Turing", "qwerty", "compLegend!", "ADMIN", "Virginia Tech")
