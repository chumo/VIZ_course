var url = "https://raw.githubusercontent.com/chumo/Data2Serve/master/transition_clusters.csv";
var myData;

function loadAndParse(data) {
  data.forEach(function(d) {
    d.Xi = +d.Xi;
    d.Yi = +d.Yi;
    d.Xf = +d.Xf;
    d.Yf = +d.Yf;
  });

  myData = data;

  // interactive
  var svg = d3.select('svg');

  svg = svg.selectAll('circle').data(myData);

  svg = svg.enter()
     .append('circle')
     .attr('cx', d => d.Xi)
     .attr('cy', d => d.Yi)
     .attr('r',5)
     .attr('fill', d => d.color);

  svg = svg.transition()
     .duration(5000)
     .attr('cx', d => d.Xf)
     .attr('cy', d => d.Yf);

  d3.selectAll('circle').on('mouseenter', function(){
    d3.select(this).transition().attr('r', 20);
  })

  d3.selectAll('circle').on('mouseout', function(){
    d3.select(this).transition().attr('r', 5);
  })

}

d3.csv(url, loadAndParse);
