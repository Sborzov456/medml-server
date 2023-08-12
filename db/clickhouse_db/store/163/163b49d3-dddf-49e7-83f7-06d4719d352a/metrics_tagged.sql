ATTACH TABLE _ UUID 'c00d55e4-92bb-40bb-8a15-9395e2e5d55b'
(
    `Date` Date,
    `Tag1` String,
    `Path` String,
    `Value` Float64,
    `Tags` Array(String),
    `Version` UInt32
)
ENGINE = ReplacingMergeTree(Version)
PARTITION BY toYYYYMM(Date)
ORDER BY (Tag1, Path, Date)
SETTINGS index_granularity = 8192
