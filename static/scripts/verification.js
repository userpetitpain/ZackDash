let c = 0;
let max = 2;
let intrvl = 1000;

setInterval(() => {
    c += 1;
    if (c >= max) {
        window.location.href = "/login";
    }
}, intrvl);