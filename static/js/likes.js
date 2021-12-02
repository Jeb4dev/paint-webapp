const callApi = (action, artwork_id) => {
    if (action !== 'add' && action !== 'remove') {
        throw new TypeError('Action can be \'add\' or \'remove\'');
    }

    fetch(`/api/likes/${action}?artwork_id=${artwork_id}`, {
        method: 'POST',
        credentials: 'include'
    });
};
