import http from "../http-common";

class BatchDataService {
    getAll() {
        return http.get("/batchs");
    }

    get(id) {
        return http.get(`/batchs/${id}`);
    }

    create(data) {
        return http.post("/batchs", data);
    }

    update(id, data) {
        return http.put(`/batchs/${id}`, data);
    }

    delete(id) {
        return http.delete(`/batchs/${id}`);
    }

    deleteAll() {
        return http.delete(`/batchs`);
    }

    findByName(name) {
        return http.get(`/batchs?name=${name}`);
    }
}

export default new BatchDataService();