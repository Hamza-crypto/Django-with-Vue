import {  createWebHistory, createRouter } from "vue-router";

import orderComponent from "@/views/Orders-All";

export default new createRouter({
    history: createWebHistory(),
    base: 'http://localhost:8081/',
    routes: [
        {
            path: '/',
            name: 'posts',
            component: orderComponent

        }
    ]
})