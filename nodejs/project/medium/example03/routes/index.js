const express = require('express');
const controller = require('../controllers/mainController');

const router = express.Router();

router.get('/profile_center', controller.profileCenterPage);
router.get('/post_detail/:id', controller.postDetailPage);
router.post('/api/posts', controller.createPost);
router.post('/api/profile/signature', controller.updateSignature);

module.exports = router;
