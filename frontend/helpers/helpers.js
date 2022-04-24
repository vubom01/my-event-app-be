export const secondToHms = (seconds) => {
  const time = Number(seconds);
  var h = Math.floor(time / 3600);
  var m = Math.floor((time % 3600) / 60);
  var s = Math.floor((time % 3600) % 60);

  var hDisplay = h > 0 ? h + " hr " : "";
  var mDisplay = m > 0 ? m + " min " : "";
  var sDisplay = s > 0 ? s + " sec" : "";
  return hDisplay + mDisplay + sDisplay;
};

export const wait = (timeout) => {
  return new Promise((resolve) => setTimeout(resolve, timeout));
};
