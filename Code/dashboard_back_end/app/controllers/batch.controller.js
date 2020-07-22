const db = require("../models");
const Batch = db.batchs;

// Create and Save a new Batch
exports.create = (req, res) => {
    // Validate request
    if (!req.body.name) {
        res.status(400).send({ message: "Name content can not be empty!" });
        return;
    }

    // Create a Batch
    const batch = new Batch({
        name: req.body.name,
        nb_bac: req.body.nb_bac,
        template: req.body.template,
        date_start : req.body.date_start,
        nb_adult: req.body.nb_adult,
        nb_laying_day: req.body.nb_laying_day,
        reproduction_humidity_mass: req.body.reproduction_humidity_mass,
        reproduction_humidity_freq: req.body.reproduction_humidity_freq,
        reproduction_humidity_type: req.body.reproduction_humidity_type,
        substrat_initial_mass: req.body.substrat_initial_mass,
        substrat_add_mass: req.body.substrat_add_mass,
        substrat_BSG: req.body.substrat_BSG,
        substrat_carrot: req.body.substrat_carrot,
        substrat_apple: req.body.substrat_apple,
        substrat_pear: req.body.substrat_pear,
        substrat_other: req.body.substrat_other,
        other_type: req.body.other_type,
        growth_humidity_mass: req.body.growth_humidity_mass,
        growth_humidity_freq: req.body.growth_humidity_freq,
        growth_humidity_type: req.body.growth_humidity_type,
        humidity_delay: req.body.humidity_delay,
        humidity_total_mass: req.body.humidity_total_mass,
        growth_day: req.body.growth_day,
        harvest_mealworm_mass: req.body.harvest_mealworm_mass,
        harvest_pupa_nb: req.body.harvest_pupa_nb,
        harvest_frass_pure: req.body.harvest_frass_pure,
        harvest_frass_filtered: req.body.harvest_frass_filtered
    });

    // Save Batch in the database
    batch
        .save(batch)
        .then(data => {
            res.send(data);
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || "Some error occurred while creating the Batch."
            });
        });
};

// Retrieve all Batchs from the database.
exports.findAll = (req, res) => {
    const name = req.query.name;
    var condition = name ? { name: { $regex: new RegExp(name), $options: "i" } } : {};

    Batch.find(condition)
        .then(data => {
            res.send(data);
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || "Some error occurred while retrieving batchs."
            });
        });
};

// Find a single Batch with an id
exports.findOne = (req, res) => {
    const id = req.params.id;

    Batch.findById(id)
        .then(data => {
            if (!data)
                res.status(404).send({ message: "Not found Batch with id " + id });
            else res.send(data);
        })
        .catch(err => {
            res
                .status(500)
                .send({ message: "Error retrieving Batch with id=" + id });
        });
};

// Update a Batch by the id in the request
exports.update = (req, res) => {
    if (!req.body) {
        return res.status(400).send({
            message: "Data to update can not be empty!"
        });
    }

    const id = req.params.id;

    Batch.findByIdAndUpdate(id, req.body, { useFindAndModify: false })
        .then(data => {
            if (!data) {
                res.status(404).send({
                    message: `Cannot update Batch with id=${id}. Maybe Batch was not found!`
                });
            } else res.send({ message: "Batch was updated successfully." });
        })
        .catch(err => {
            res.status(500).send({
                message: "Error updating Batch with id=" + id
            });
        });
};

// Delete a Batch with the specified id in the request
exports.delete = (req, res) => {
    const id = req.params.id;

    Batch.findByIdAndRemove(id)
        .then(data => {
            if (!data) {
                res.status(404).send({
                    message: `Cannot delete Batch with id=${id}. Maybe Batch was not found!`
                });
            } else {
                res.send({
                    message: "Batch was deleted successfully!"
                });
            }
        })
        .catch(err => {
            res.status(500).send({
                message: "Could not delete Batch with id=" + id
            });
        });
};

// Delete all Batchs from the database.
exports.deleteAll = (req, res) => {
    Batch.deleteMany({})
        .then(data => {
            res.send({
                message: `${data.deletedCount} Batchs were deleted successfully!`
            });
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || "Some error occurred while removing all batchs."
            });
        });
};

// Find all published Batchs
exports.findAllPublished = (req, res) => {
    Batch.find({ published: true })
        .then(data => {
            res.send(data);
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || "Some error occurred while retrieving batchs."
            });
        });
};
