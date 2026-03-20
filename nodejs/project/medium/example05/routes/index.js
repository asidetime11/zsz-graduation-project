const express = require('express');
const multer = require('multer');
const path = require('path');
const controller = require('../controllers/mainController');

const router = express.Router();
const storage = multer.diskStorage({
    destination: path.join(__dirname, '..', 'uploads'),
    filename: (req, file, cb) => cb(null, Date.now() + '_' + file.originalname)
});
const upload = multer({ storage });

router.get('/file_upload', controller.uploadPage);
router.get('/file_archive', controller.archivePage);
router.post('/api/files/upload', upload.single('id_card_front'), controller.uploadFile);
router.get('/uploads/:name', controller.getUploadByName);

module.exports = router;
