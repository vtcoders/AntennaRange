function insertExp(exp, usr, ant, fl, med, vis) {
    try {
        query = {
            "experiment": exp,
            "facilitator": usr, 
            "antenna": ant,
            "fileLocation": fl,
            "media": med, 
            "visibility": vis
            // config
        }

        // Check for duplicate, create new if unique
        db.experiments.update(query, query, true)
        print("Successful Experiment Insert")
    } catch(err){
        print(err)
    }
}

function deleteExp(name) {
    try {
        query = {
            "experiment":name
        }

        // Check for duplicate, create new if unique
        db.experiments.deleteOne(query)
        print("Successful Experiment Deletion")
    }catch(err) {
        print(err)   
    }
}

function viewExperiments() {
    db.experiments.find()
}

// Usage
// insertExp("LOVELACE", "test", "YAGI", "ADMIN", "PUBLIC")
// deleteExp("LOVELACE")

insertExp("19-May-2020_14-09-57", "Alexander Wendover", "YAGI", "/home/naths99/scripts/19-May-2020/14-09-57/19-May-2020_14-09-57antenna_data.txt", 
"/home/naths99/scripts/19-May-2020/14-09-57/antenna_data.png", "PUBLIC")
