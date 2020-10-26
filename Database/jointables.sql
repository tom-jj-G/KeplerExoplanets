-- View all the initial data
SELECT *
FROM kepler_habitable AS t
INNER JOIN raw_kepler AS v ON (t.kepid=v.kepid) 