function insertExp(exp, usr, ant, fl, vis) {
    try {
        query = {
            "experiment": exp,
            "facilitator": usr, 
            "antenna": ant,
            "fileLocation": fl, 
            "visibility": vis
            // config
            // media
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

// insertExp("LOVELACE", "test", "YAGI", "ADMIN", "PUBLIC")
// deleteExp("LOVELACE")
