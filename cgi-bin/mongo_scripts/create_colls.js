// https://docs.mongodb.com/manual/reference/method/db.createCollection/#create-a-collection-with-document-validation

// Creates collection for users
db.createCollection("accounts", {
    validator: { "$jsonSchema": {
            bsonType: "object",
            required: [ "name", "username", "password", "group", "organization" ],
            properties: {
                name: {
                    bsonType: "string",
                    description: "First Name and Last Name. Must be a string and is required"
                },
                username: {
                    bsonType: "string",
                    description: "Login Credential. Must be a string and is required"
                },
                password: {
                    bsonType: "string",
                    description: "Login Credential. Must be a string and is required"
                },
                group: {
                    enum: [ "ADMIN", "INSTRUCTOR", "USER"],
                    description: "Can only be one of the enum values and is required"
                },
                organization: {
                    bsonType: "string",
                    description: "Must be a string and is required"
                }
            }
        }},
    validationLevel: "moderate",
    validationAction: "error"
})


// Creates collection for experiments
db.createCollection("experiments", {
    validator: { "$jsonSchema": {
            bsonType: "object",
            required: [ "experiment", "facilitator", "antenna", "fileLocation", "visibility" ], //TODO
            properties: {
                experiment: {
                    bsonType: "string",
                    description: "Must be a string and is required"
                },
                facilitator: {
                    bsonType: "string", //"object",
                    description: "Must be a User in Database"
                },
                antenna: {
                    enum: [ "YAGI"],
                    description: "Can only be one of the enum values and is required"
                },
                fileLocation: {
                    bsonType: "string",
                    description: "Must be a string and is required"
                },
                config: { //TODO
                    bsonType: "string",
                    description: "Must be a string and is required"
                },
                media: { //TODO
                    bsonType: "string",
                    description: "Must be a string and is required"
                },
                visibility: {
                    enum: [ "PUBLIC", "Private"],
                    description: "Can only be one of the enum values and is required"
                },
            }
        }
    },
    validationLevel: "moderate",
    validationAction: "error"
})

