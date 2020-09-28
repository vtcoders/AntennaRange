# Antenna Range - Database Management with MongoDB

**Contents**<br>
[Documentation](#documentation)<br>
[Running and Compiling](#running-and-compiling)<br>

## Documentation
Implemented by [Mongo Shell](https://docs.mongodb.com/manual/tutorial/write-scripts-for-the-mongo-shell/)

## Running and Compiling
### Application
Run the `mongo` shell with database name<br>
```
mongo [DB_Name]
```

`load()` the corresponding script<br>
```
load("create_colls.js")
```

Verify collection existence<br>
```
show collections
db.getCollectionInfos()
```
