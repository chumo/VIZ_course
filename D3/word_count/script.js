function myFunction(s) {
    var s = d3.select('#myText').text();

    var removePunctuation = s.replace(/[!,?.":;]/g, ' ');
    var split = removePunctuation.trim().split(" ");

    var res = _.pairs(_.countBy(split));
    res = _.filter(res, function(d){return d[0]!=String.fromCharCode(160);});
    res = _.sortBy(res, function(d){return -d[1];})

    var words = d3.selectAll('div').data(res);

    words.text(function(d) {return d[0];})
        // .transition().duration(500)
        .style('font-size', function(d) {return d[1] * 24 + 'pt'});

    words.enter()
        .append('div')
        .style('text-align','center')
        .text(function(d) {return d[0];})
        .style('font-size', function(d) {return d[1] * 24 + 'pt'});

    words.exit()
        .remove();

}
