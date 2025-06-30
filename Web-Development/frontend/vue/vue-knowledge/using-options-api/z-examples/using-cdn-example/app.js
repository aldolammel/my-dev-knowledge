
Vue.createApp({
  data() {
    return {
      currentYear: new Date().getFullYear(),  // output e.g: 2025
      name: 'Aldo Lammel',
      born: 1984,
      img: 'https://scontent.fpoa35-1.fna.fbcdn.net/v/t39.30808-1/356106573_10230555841903209_5737810450586874016_n.jpg?stp=dst-jpg_s200x200_tt6&_nc_cat=103&ccb=1-7&_nc_sid=e99d92&_nc_eui2=AeG1vpMw6lchZrO5ONaTnwefRhNquEild0lGE2q4SKV3SV_xNvL-fgaNF2KWOBJE9HA&_nc_ohc=-_dQrIaM2OAQ7kNvwHP2edX&_nc_oc=AdnkxoWzM6NsqVQ23wwANcr6uixXHUVAXBUJ1_qhRif4lTwUs3vjYzPI7ofdzEzNCVM&_nc_zt=24&_nc_ht=scontent.fpoa35-1.fna&_nc_gid=4XY8uueDg8YQVMudODIWAA&oh=00_AfNCozRdVph-nwQVHJPXhVU5FqRpL4hgRg6p5Xqv-Sx5sQ&oe=68634537'
    }
  },
  methods: {
    userAge(year) {
      if (!year) {
        year = this.currentYear;
      };
      return (year - this.born);
    }    
  }
}).mount('#assignment');