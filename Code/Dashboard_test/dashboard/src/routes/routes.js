import Vue from 'vue'
import Router from 'vue-router'
import Accueil from '../layout/Accueil';
import Data from "../layout/Data";
import Calendar from "../layout/Calendar";
import Insert from "../layout/Insert";
import Stock from "../layout/Stock";
import Task from "../layout/Task";
import Measure from "../layout/Measure";

Vue.use(Router)

export default new Router({
    routes:[
        {
            path: '/',
            name: 'Accueil',
            component: Accueil
        },
        {
            path: '/Data',
            name: 'Data',
            component: Data
        },
        {
            path: '/Calendar',
            name: 'Calendar',
            component: Calendar
        },
        {
            path: '/Insert',
            name: 'Insert',
            component: Insert
        },
        {
            path: '/Stock',
            name: 'Stock',
            component: Stock
        },
        {
            path: '/Task',
            name: 'Task',
            component: Task
        },
        {
            path: '/Measure',
            name: 'Measure',
            component: Measure
        }

    ]
})