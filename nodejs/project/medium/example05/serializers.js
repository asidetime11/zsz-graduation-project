function serializeEmployeeFileAllFields(file) {
    return {
        id: file.id,
        employee_id: file.employee_id,
        id_card_front: file.id_card_front,
        id_card_back: file.id_card_back,
        labor_contract: file.labor_contract,
        avatar_frame_style: file.avatar_frame_style
    };
}

module.exports = { serializeEmployeeFileAllFields };
