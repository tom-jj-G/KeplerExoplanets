-- Table: public.raw_kepler

-- DROP TABLE public.raw_kepler;

CREATE TABLE public.raw_kepler
(
    rowid integer NOT NULL,
    kepid integer NOT NULL,
    kepoi_name text COLLATE pg_catalog."default" NOT NULL,
    kepler_name text COLLATE pg_catalog."default",
    koi_disposition text COLLATE pg_catalog."default" NOT NULL,
    koi_pdisposition text COLLATE pg_catalog."default" NOT NULL,
    koi_score double precision,
    koi_fpflag_nt bigint,
    koi_fpflag_ss bigint,
    koi_fpflag_co bigint,
    koi_fpflag_ec bigint,
    koi_period double precision,
    koi_period_err1 double precision,
    koi_period_err2 double precision,
    koi_time0bk double precision,
    koi_time0bk_err1 double precision,
    koi_time0bk_err2 double precision,
    koi_impact double precision,
    koi_impact_err1 double precision,
    koi_impact_err2 double precision,
    koi_duration double precision,
    koi_duration_err1 double precision,
    koi_duration_err2 double precision,
    koi_depth double precision,
    koi_depth_err1 double precision,
    koi_depth_err2 double precision,
    koi_prad double precision,
    koi_prad_err1 double precision,
    koi_prad_err2 double precision,
    koi_teq double precision,
    koi_teq_err1 double precision,
    koi_teq_err2 double precision,
    koi_insol double precision,
    koi_insol_err1 double precision,
    koi_insol_err2 double precision,
    koi_model_snr double precision,
    koi_tce_plnt_num double precision,
    koi_tce_delivname text COLLATE pg_catalog."default",
    koi_steff double precision,
    koi_steff_err1 double precision,
    koi_steff_err2 double precision,
    koi_slogg double precision,
    koi_slogg_err1 double precision,
    koi_slogg_err2 double precision,
    koi_srad double precision,
    koi_srad_err1 double precision,
    koi_srad_err2 double precision,
    ra double precision,
    "dec" double precision,
    koi_kepmag double precision,
    CONSTRAINT pk_raw_kepler PRIMARY KEY (kepoi_name)
)

TABLESPACE pg_default;

ALTER TABLE public.raw_kepler
    OWNER to postgres;
