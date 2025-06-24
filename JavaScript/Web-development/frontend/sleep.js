

// TRUE SLEEP WITH JAVASCRIPT:

sleep(ms) {
    // This function is just a sleep for JS.
    // Use it as: await this.sleep(<duration in miliseconds>);
    return new Promise(resolve => setTimeout(resolve, ms));
},