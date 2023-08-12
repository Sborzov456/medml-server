ATTACH TABLE _ UUID 'c4626ff7-841f-45a5-a249-1c3e875ac061'
(
    `Tag1` String,
    `Path` String,
    `Value` Float64,
    `Time` UInt32,
    `Date` Date,
    `Timestamp` UInt32
)
ENGINE = GraphiteMergeTree('graphite_rollup')
PARTITION BY toYYYYMM(Date)
ORDER BY (Path, Time)
SETTINGS index_granularity = 8192
