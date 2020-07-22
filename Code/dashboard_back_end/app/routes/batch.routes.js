module.exports = app => {
    const batchs = require("../controllers/batch.controller.js");

    var router = require("express").Router();

    // Create a new Tutorial
    router.post("/", batchs.create);

    // Retrieve all Tutorials
    router.get("/", batchs.findAll);

    // Retrieve all published Tutorials
    router.get("/published", batchs.findAllPublished);

    // Retrieve a single Tutorial with id
    router.get("/:id", batchs.findOne);

    // Update a Tutorial with id
    router.put("/:id", batchs.update);

    // Delete a Tutorial with id
    router.delete("/:id", batchs.delete);

    // Create a new Tutorial
    router.delete("/", batchs.deleteAll);

    app.use('/api/batchs', router);
};