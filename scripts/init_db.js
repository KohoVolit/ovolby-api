/* A script to initialize a database.
*
* Use in TokuMX shell ($ mongo)
*
* > use <db-name>
* > load("<absolute-path>/init_db.js")
*/

// create indexes on Areas
db.createCollection("areas", {"primaryKey": {"id": 1, "_id": 1}});
db.areas.ensureIndex({"name": 1});
db.areas.ensureIndex({"identifier": 1});
db.areas.ensureIndex({"classification": 1});

// create indexes on Elections
db.createCollection("elections", {"primaryKey": {"id": 1, "_id": 1}});
db.areas.ensureIndex({"name": 1});
db.areas.ensureIndex({"organization_id": 1});


// create indexes on Organizations
db.createCollection("organizations", {"primaryKey": {"id": 1, "_id": 1}});
db.organizations.ensureIndex({"name": 1});
db.organizations.ensureIndex({"identifiers.identifier": 1});
db.organizations.ensureIndex({"classification": 1});
db.organizations.ensureIndex({"parent_id": 1});
db.organizations.ensureIndex({"areas.area_id":1, "areas.election_id":1}, {"unique": true, "sparse": true})

//create indexes on Results
db.createCollection("results", {"primaryKey": {"_id": 1}});
db.results.ensureIndex({"election_id": 1, "area_id": 1}, {"unique": true, "sparse": true});

// create indexes on Options
db.createCollection("options", {"primaryKey": {"id": 1, "_id": 1}});
db.options.ensureIndex({"name": 1});
db.options.ensureIndex({"type": 1});
db.options.ensureIndex({"election_id": 1, "area_id": 1}, {"unique": true, "sparse": true});


